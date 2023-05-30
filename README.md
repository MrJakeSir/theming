
# colormate
Python script text formatting package

## What is colormate?
colormate is a **python library** that lets you add text formatting to your scripts,
its very easy to use, you can also use hex colors (for example: "#ffffff"), rgb 
tuples (for example: (255, 255, 255) ), or you can use the name of the color 
(for example: 'White')
### Platform availability
This package will only work on **(gnu)linux and macOSX systems**, thats because
this script uses ansi escapes that only works on these systems, and this script
**requires a true color compatible terminal**, so you  can get the rgb colors 
working. If you don't have a true color compatible terminal, you can use the colors
by their names, like 'White', 'Yellow', etc. If you want to get a full list of colors,
you can use ``self.get_colors()`` method, which will return a list with all the available
colors


## Installation
```bash
pip install colormate
```

## Usage
```py
import colormate

mythemeobject = colormate.Theme()

## Get documentation
mythemeobject.__doc__

## Colorize method
mythemeobject.colorize(
    'This text has beautiful colors!',
    fg = '#ff00ff',
    bg = '#000000'
)
# fg and bg arguments are both optional, you can add a background color
# without setting a foreground color first and vice versa
```

![FirstExample](https://i.imgur.com/OtQIm6P.png)

You can also use color names

```py
obj = colormate.Theme()
print(
    'My colorized text is', 
    obj.colorize(
        'this', 
        fg = 'Blue',
        bg = 'Black'    
    )
)

```

![NameExample](https://i.imgur.com/1QuGBCj.png)

As you can see, if you use the color names directly, it will use the colors associated to your terminal, contrary to when
you set the colors directly with a rgb color

You can also use an rgb tuple

```py
print(
    'My colorized text is', 
    obj.colorize(
        'this', 
        fg = (0, 0, 255),
        bg = (0, 0, 0)  
    )
)
```
![TupleExample](https://i.imgur.com/qj68FQj.png)

### Text formatting
These are the available formmating methods

```py
from colormate import Theme
Theme().bold           ("This will return a bold string!")  
Theme().dim            ("This will return a dim string!") 
Theme().italic         ("This will return an italic string!") 
Theme().underlined     ("This will return an underlined string!") 
Theme().blinking       ("This method [is useless]") 
Theme().reversed       ("This will reverse background and foreground colors") 
Theme().invisible      ("This method will return an invisible string so [it is also useless]") 
```

### License
MIT LICENSE
```
Copyright (c) 2021 Rodrigo
All rights reserved.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

