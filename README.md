# vos
## POSIX System Command Executor

### Description:
  Library for executing Shell commands, returning information about the execution status, and the generated output to the caller!

### Installation

  ```shell
  git clone https://github.com/viniciusfdasilva/vos.git
  ```
  ```shell
  cd vos
  ```
  ```shell
  sudo make install python_path=[PYTHON_LIB_PATH]
  ```
### About Library
*************************
Name: vos

Author: Vinicius Silva

Version: 0.1

Release Year: 2024
*************************

### Remove

  ```shell
  sudo make remove python_path=[PYTHON_LIB_PATH]
  ```

### Using
  
   ```python
    import vos
    
    os_result = vos.OS._system('ls -la')
   
    print(os_result.exit_code)
    print(os_result.output)
   ```
   or
   
   ```python
   from vos import OS
   
   os_result = OS._system('ls -la')

   print(os_result.exit_code)
   print(os_result.output)
   ```

  
