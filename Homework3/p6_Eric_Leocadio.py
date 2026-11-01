# PROBLEM 6
"""Storage hierarchy classes and demonstration for Homework 3."""

from __future__ import annotations

import sys
import unittest


# PART A: Base entry class.
class Entry:
    """Represent an entry in a storage hierarchy."""

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        """Initialize an entry.

        Args:
            name: Display name for the entry.
            parent: Parent entry, or None when this entry is a root.

        Preconditions:
            name is a string. If parent is supplied, it is an Entry or None.

        Postconditions:
            Stores name and parent in the new Entry.
        """
        self.name: str = name
        self._parent: Entry | None = parent

    def parent(self) -> Entry | None:
        """Return this entry's parent.

        Preconditions:
            The entry has been initialized.

        Postconditions:
            Returns the parent Entry, or None when the entry is a root.
        """
        return self._parent

    def size(self) -> int:
        """Return the storage size represented by this entry.

        Preconditions:
            Called on a concrete Entry subclass.

        Postconditions:
            Returns the entry's size according to its subclass.
        """
        raise NotImplementedError("Subclasses must implement size().")

    # PART C: Recursive absolute path from current entry through the root.
    def absolute_path(self) -> list[Entry]:
        """Return this entry and its ancestors from current entry to root.

        Preconditions:
            The entry's parent links, if any, contain no cycles.

        Postconditions:
            Returns a new list beginning with this entry and ending at the
            top-most ancestor.
        """
        parent: Entry | None = self.parent()
        if parent is None:
            return [self]
        return [self] + parent.absolute_path()


# PART A: File subclass.
class File(Entry):
    """Represent a file with a nonnegative size in bytes."""

    def __init__(
        self, name: str, bytes_used: int, parent: Entry | None = None
    ) -> None:
        """Initialize a file and validate its byte count.

        Args:
            name: Display name for the file.
            bytes_used: Number of bytes occupied by the file.
            parent: Parent folder, or None when the file is unattached.

        Preconditions:
            bytes_used is an integer greater than or equal to zero.

        Postconditions:
            Creates a File with name, parent, and byte count stored.

        Raises:
            ValueError: If bytes_used is negative.
        """
        super().__init__(name, parent)
        if bytes_used < 0:
            raise ValueError("bytes_used must be nonnegative")
        self.bytes_used: int = bytes_used

    def size(self) -> int:
        """Return the number of bytes used by this file.

        Preconditions:
            The file was initialized with a valid nonnegative byte count.

        Postconditions:
            Returns bytes_used unchanged.
        """
        return self.bytes_used


# PART B: Folder subclass.
class Folder(Entry):
    """Represent a folder that contains other entries."""

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        """Initialize an empty folder.

        Args:
            name: Display name for the folder.
            parent: Parent folder, or None when this folder is a root.

        Precondition:
            name is a string and parent is an Entry or None.

        Postcondition:
            Creates an empty folder with the supplied name and parent.
        """
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Add an entry to this folder.

        Args:
            entry: Entry to attach as a direct child.

        Preconditions:
            entry is an Entry, and the resulting hierarchy has no cycle.

        Postconditions:
            Adds entry to the folder's child list and sets entry's parent to
            this folder.
        """
        entry._parent = self
        self._children.append(entry)

    def children(self) -> tuple[Entry, ...]:
        """Return all direct child entries in insertion order.

        Preconditions:
            The folder has been initialized.

        Postconditions:
            Returns a tuple snapshot of direct children. The original folder
            list is not exposed or mutated by this method.
        """
        return tuple(self._children)

    def size(self) -> int:
        """Return the total size of all direct and nested children.

        Preconditions:
            The folder hierarchy contains no cycles and each entry has a
            valid size implementation.

        Postconditions:
            Returns the sum obtained by polymorphically calling size() on each
            direct child, including nested folder totals.
        """
        return sum(child.size() for child in self._children)


# PART D: Recursive large-file search.
def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Recursively return qualifying File objects below the starting entry.

    Args:
        entry: Starting file or folder.
        minimum_size: Inclusive minimum file size in bytes.

    Preconditions:
        entry is an Entry, minimum_size is an integer, and folder structures
        contain no cycles.

    Postconditions:
        If entry is a File, returns it when its size is at least minimum_size
        and otherwise returns an empty list. If entry is a Folder, recursively
        searches its children and returns qualifying nested File objects.
        Entries above the starting entry and siblings outside its subtree are
        not searched.
    """
    if isinstance(entry, File):
        if entry.size() >= minimum_size:
            return [entry]
        return []

    if isinstance(entry, Folder):
        found: list[File] = []
        for child in entry.children():
            found.extend(find_large_files(child, minimum_size))
        return found

    return []


# PART E: Unit tests for parts c and d.
class FindLargeFilesTests(unittest.TestCase):
    """Test find_large_files for file and folder starting entries."""

    def setUp(self) -> None:
        """Build a small hierarchy before each test.

        Precondition:
            The test case instance has been created.

        Postcondition:
            Initializes test entries and parent-child relationships.
        """
        self.root = Folder("root")
        self.documents = Folder("documents")
        self.photo = File("photo.jpg", 500)
        self.notes = File("notes.txt", 120)
        self.backup = File("backup.zip", 1500)

        self.root.add(self.documents)
        self.documents.add(self.notes)
        self.documents.add(self.photo)
        self.root.add(self.backup)

    def test_file_entry_meets_threshold(self) -> None:
        """Verify that a qualifying starting file is returned.

        Precondition:
            setUp() created the hierarchy.

        Postcondition:
            Asserts the exact file match list.
        """
        self.assertEqual(find_large_files(self.backup, 1500), [self.backup])

    def test_file_entry_below_threshold(self) -> None:
        """Verify that a starting file below the threshold is excluded.

        Precondition:
            setUp() created the hierarchy.

        Postcondition:
            Asserts that the result is an empty list.
        """
        self.assertEqual(find_large_files(self.notes, 500), [])

    def test_folder_search_is_recursive(self) -> None:
        """Verify recursive folder search includes nested qualifying files.

        Precondition:
            setUp() created direct and nested test entries.

        Postcondition:
            Asserts the exact list of files meeting the threshold.
        """
        self.assertEqual(
            find_large_files(self.root, 500),
            [self.photo, self.backup],
        )

    def test_no_large_files(self) -> None:
        """Verify that an unmatched threshold returns an empty list.

        Precondition:
            setUp() created the hierarchy.

        Postcondition:
            Asserts that no file meets the threshold.
        """
        self.assertEqual(find_large_files(self.root, 2000), [])


class AbsolutePathTests(unittest.TestCase):
    """Test absolute paths for root and nested entries."""

    def setUp(self) -> None:
        """Build a nested hierarchy before each test.

        Precondition:
            The test case instance has been created.

        Postcondition:
            Initializes nested folders and a file with parent links.
        """
        self.root = Folder("root")
        self.level_one = Folder("level_one")
        self.level_two = Folder("level_two")
        self.file = File("data.txt", 42)

        self.root.add(self.level_one)
        self.level_one.add(self.level_two)
        self.level_two.add(self.file)

    def test_root_path(self) -> None:
        """Verify that a root entry's path contains only itself.

        Postcondition:
            Asserts the root entry is the sole list element.
        """
        self.assertEqual(self.root.absolute_path(), [self.root])

    def test_nested_file_path(self) -> None:
        """Verify the nested file path is ordered toward the root.

        Postcondition:
            Asserts the file-to-root Entry list in exact order.
        """
        self.assertEqual(
            self.file.absolute_path(),
            [self.file, self.level_two, self.level_one, self.root],
        )


def run_unit_tests() -> None:
    """Run all unit tests contained in this module.

    Precondition:
        The unittest classes have been loaded in this module.

    Postcondition:
        Displays test results and returns without altering the hierarchy classes.
    """
    suite = unittest.defaultTestLoader.loadTestsFromModule(
        sys.modules[__name__]
    )
    unittest.TextTestRunner(verbosity=2).run(suite)


def main() -> None:
    """Run tests and demonstrate the storage hierarchy.

    Precondition:
        The module's Entry, File, Folder, and helper classes are available.

    Postcondition:
        Runs embedded unit tests, constructs a three-level hierarchy, and
        prints total size, threshold search results, and an absolute path.
    """
    # PART F: Construct the demonstration hierarchy three folders deep.
    run_unit_tests()
    root: Folder = Folder("root")
    documents: Folder = Folder("documents")
    photos: Folder = Folder("photos")
    archives: Folder = Folder("archives")

    small: File = File("notes.txt", 120)
    medium: File = File("photo.jpg", 500)
    large: File = File("backup.zip", 1500)

    root.add(documents)
    documents.add(small)
    documents.add(photos)
    photos.add(medium)
    photos.add(archives)
    archives.add(large)

    # PART F: One polymorphic size() call sums every File and nested Folder.
    print("Outer folder size:", root.size())
    print("Files of at least 500 bytes:", [
        item.name for item in find_large_files(root, 500)
    ])
    print("Files of at least 1000 bytes:", [
        item.name for item in find_large_files(root, 1000)
    ])

    # PART G: Demonstrate absolute_path() using the hierarchy from part f.
    print("Absolute path for backup.zip:", [
        entry.name for entry in large.absolute_path()
    ])


if __name__ == "__main__":
    main()