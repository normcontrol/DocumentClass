# DocumentClass

## Description 

Repository describing unified classes representing the structural elements of a text document

## Install


## How use

```python
from Paragraph import Paragraph
from helpers.EnumFill import EnumFill

para = Paragraph(text=" 123 ", indent=" 1", lineSpacing=1, fontName=" 123", textSize='12',
              nochangeFontName=True, nochangeTextSize=False,
              alignment=None, mrgrg=None, mrglf=None, mrgtop=None, mrgbtm=None, bold=None,
              italics=EnumFill(1),
              underlining=2, subText=None, superText=None, colorText="White",
              keepLinesTogether=None, keepWithNext=None, outlineLevel=None,
              noSpaceBetweenParagraphsOfSameStyle=None, pageBreakBefore=None)

```


## Project structure

```
DocumentClass/
├── README.md
├── DocumentClass.py
├── DrawFrame.py
├── Paragraph.py
├── Table.py
├── TableCell.py
├── TableColumn.py
├── TableRow.py
├── helpers/
│   ├── __init__.py
│   ├── EnumFill.py
└── 
    
```