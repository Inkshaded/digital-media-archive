# Design Patterns
## SOLID Design Principles
### Single Responsibility Principle
Below, all functional program files will be summarised simply to demonstrate adherence to the Single Responsibility Principle
```
Program Files

implementations/ # holds concrete behaviors
    csv_record_store : Implementation of RecordStorage that creates/appends to
    a 'records' file to keep track of when and what has been archived
    local_storage.py : Implementation of Storage that archives files locally
    tkinter_file_selector.py : Implementation of FileSelector that opens a
    tkinter dialog box to select a file

ui/
    ui_start.py : Handles Tkinter UI layout and updates

controller_interface.py : defines abstractions for FileSelector and Storage

main.py : Acts as controller, in charge of interactions between UI and logic
```
### Open/Closed Principle
Storage, RecordStore, and FileSelector can all be extended, as they are utilized by the controller in main.py through their abstract interfaces, as defined in controller_interface.py. Additionally, this means that if an additional implementation were added to, say, store files in the cloud, the local_storage.py implementation could remain unchanged.

### Liskov Substitution Principle
Any implementation of Storage, FileSelector, or RecordStore can be implemented through the controller_interface.py definitions

### Interface Segregation Principle
The interfaces in the program are kept tiny and seperate from one another, minimizing dependencies.

Existing dependencies:
```
ArchiveApp (controller)
|-- depends on -> FileSelector.select_file()
|-- depends on -> Storage.save() 
|-- depends on -> RecordStore.append(), RecordStore.read_tail
```
Implementations of interfaces:

    TkFileSelector ->  implements -> FileSelector

    LocalStorage ->  implements -> Storage

    CsvRecordStore -> implements -> RecordStore

### Dependency Inversion Principle
The high-level controller only relies on the abstractions of the FileSelector, Storage, and RecordStore interfaces. The actual details of how the concrete implementations work only matter at the lower level and are therefore only accessed there. For example, LocalStorage implementation can be directly applied to the program through the Storage interface, but not vice versa.

## Other Design Patterns

### Singleton

### Factory Method

### Abstract Factory

### Proxy

### Prototype

### Object Pool

### Iterator

### Facade

### Builder

### Bridge

### Composite

### Chain of Responsibility

### Filter

### Adapter
