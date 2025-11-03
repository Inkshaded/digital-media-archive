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


### Dependency Inversion Principle


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
