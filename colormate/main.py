from sys import platform as OS
import re

class Theme:
    """
Theming class 
available methods:
    self.bold           (text: str)  
    self.dim            (text: str) 
    self.italic         (text: str) 
    self.underlined     (text: str) 
    self.blinking       (text: str) 
    self.reversed       (text: str) 
    self.invisible      (text: str) 

    self.colorize       (text: str, **kwargs):
    """
    def __init__(self):
        
        self._INTEGERS       = {
            'Normal':           0,
            'Bold':             1,
            'Dim':              2,
            'Italic':           3,
            'Underlined':       4,
            'Blinking':         5,
            'Reverse':          7,
            'Invisible':        8
        }
        
        self._COLORS         = {
            'Default':          9,
            'Black':            0,
            'Red':              1,
            'Green':            2,
            'Yellow':           3,
            'Blue':             4,
            'Magenta':          5,
            'Cyan':             6,
            'Light gray':       7,
            'Dark gray':        60,
            'Light red':        61,
            'Light green':      62,
            'Light yellow':     63,
            'Light blue':       64,
            'Light magenta':    65,
            'Light cyan':       66,
            'White':            67
        }

        self._escape    = '\x1B[' if OS == 'darwin' else '\033['
        self._no_color  = '\033[0m'       
        self._to_rgb    = lambda h: tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        self._format    = lambda code, text:    self._escape    + \
                                                str(code)       + \
                                                'm'             + \
                                                text            + \
                                                self._no_color  
        self.get_colors = lambda: list(self._COLORS.keys()) 
        self.bold       = lambda text: self._format(self._INTEGERS['Bold'], text)   
        self.dim        = lambda text: self._format(self._INTEGERS['Dim'], text)   
        self.italic     = lambda text: self._format(self._INTEGERS['Italic'], text)   
        self.underlined = lambda text: self._format(self._INTEGERS['Underlined'],text)
        self.blinking   = lambda text: self._format(self._INTEGERS['Blinking'], text) 
        self.reversed   = lambda text: self._format(self._INTEGERS['Reverse'], text) 
        self.invisible  = lambda text: self._format(self._INTEGERS['Invisible'], text) 
        

    def _to_escape(self, r, g, b, bg=False):
        if not bg:
            return f'38;2;{r};{g};{b}'

        return f'48;2;{r};{g};{b}'

    def colorize(self, text: str, **kwargs):
        """
self.colorize(text: str, **kwargs) 
kwargs options:
    bg = hex value | rgb tuple code | color name 
    fg = hex value | rgb tuple code | color name 

    hex value example:
        '#ffffff'   -> White color 
                    -> It also should always have the hash symbol

    rgb tuple code example:
        (255, 255, 255) 
                    -> White color 
                    -> It should have only three items 
                    -> First item represents red, second item represents green and last item represents blue 

    color name example:
        'White'     -> White color 
                    -> Available colors are:
                        [
                            'Default',
                            'Black',
                            'Red',
                            'Green',
                            'Yellow',
                            'Blue',
                            'Magenta',
                            'Cyan',
                            'Light gray',
                            'Dark gray',
                            'Light red',
                            'Light green',
                            'Light yellow',
                            'Light blue',
                            'Light magenta',
                            'Light cyan'
                        ]
        """

        colors = self._COLORS
        fg = colors['Default']*30
        bg = colors['Default']*40
        
        for key, value in kwargs.items():
            if type(value) == tuple:
                if key == 'bg':
                    bg = self._to_escape(*value, bg=True) 
                else:
                    fg =self._to_escape(*value)  

            elif re.match('#[a-fA-F0-9]{6}', value):
                value = value.replace('#', '')
                if key == 'bg':
                    bg = self._to_escape(*self._to_rgb(value), bg=True) 
                else:
                    fg = self._to_escape(*self._to_rgb(value))
            
            elif value in self._COLORS.keys():
                if key == 'bg':
                    bg = self._COLORS[value]+40
                else:
                    fg = self._COLORS[value]+30

        
        return self._format(fg, self._format(bg, text))

