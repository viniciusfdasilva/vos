import os

class OSResult():
    
    def __init__(self, exit_code, output):
        
        self.exit_code = exit_code
        self.output    = output        
        
class OS():    
    
    __path         = '/tmp/'
    __filename     = '.os_result'
    __EXIT_FAILURE = 1
    
    @staticmethod
    def __panic(message : str):
        """
        Print e message and exit the program with error status
        """
        print(message)
        exit(OS.__EXIT_FAILURE)
        
    @staticmethod
    def __readfile() -> str:
        """
        Read output file and return a string with a last
        command executed by _system(cmd: str) function
        """
        try:
            output = ''
        
            if not os.path.exists(f'{OS.__path}{OS.__filename}'):
                
                os.system(f'touch {OS.__path}{OS.__filename}')

            file = open(f'{OS.__path}{OS.__filename}', 'r')

            output = file.read()
            output = output[0:len(output)-1]

            file.close()
        except Exception:
            
            OS.__panic('Output read error!')
        
        return output
        
    @staticmethod     
    def _system(cmd : str) -> OSResult:
        """
        Execute a shell command redirecting output text from output file.
        Obtain a status code and the output text and return a OSResult object
        """
        if os.name == 'posix':
            
            exit_code = os.system(f"{cmd} > {OS.__path}{OS.__filename}")
            output    = OS.__readfile()
            return OSResult(exit_code=exit_code, output=output)

        else:
            OS.__panic('Plataform not support!')
