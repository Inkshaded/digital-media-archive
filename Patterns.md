# Design Patterns
## SOLID Design Principles
### Single Responsibility Principle
Below, all functional program files will be summarised simply to demonstrate adherence to the Single Responsibility Principle
```
Program Files

implementations/ # holds concrete behaviors
    local_storage.py : Implementation of Storage that archives files locally
    tkinter_file_selector.py : Implementation of FileSelector that opens a
    tkinter dialog box to select a file

ui/
    ui_start.py : Handles Tkinter UI layout and updates

controller_interface.py : defines abstractions for FileSelector and Storage

main.py : Acts as controller, in charge of interactions between UI and logic
```
### Open/Closed Principle
The ArchiveApp class (controller) is only dependent on the FileSelector and Storage abstract interfaces, meaning that the controller does not need to be changed to modify the implementation of the program.

### Liskov Substitution Principle


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
