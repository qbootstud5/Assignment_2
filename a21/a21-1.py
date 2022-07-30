#!/usr/bin/env python
"""Assignment 2 Part 1 starter"""

from typing import IO

class HtmlDoc:
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, window_title: str) -> None:
        self.__fnam: str = file_name
        self.__wintitle: str = window_title
        self.fd: IO[str] = self.open_html_file()

    def generate_html_file(self) -> None:
        """write_html_file method"""
        self.write_html_head()
        self.write_html_tail()
        
    def open_html_file(self) -> None:
        return open(self.__fnam, "w")

    def close_html_file(self) -> None:
        self.fd.close()

    def __write_html_comment(self, t: int, com: str) -> None:
        """write_html_comment method"""
        ts: str = HtmlDoc.TAB * t
        self.fd.write(f"{ts}<!--{com}-->\n")
        
    def write_html_line(self, t: int, line: str) -> None:
        """write_thml_line method"""
        ts: str = HtmlDoc.TAB * t
        self.fd.write(f"{ts}{line}\n")

    def write_html_head(self) -> None:
        """write_html_header method"""
        self.write_html_line(0, "<html>")
        self.write_html_line(0, "<head>")
        self.write_html_line(1, f"<title>{self.__wintitle}</title>")
        self.write_html_line(0, "</head>")
        self.write_html_line(0, "<body>")
        self.__write_html_comment(1, "to be generated")

    def write_html_tail(self) -> None:
        self.write_html_line(0, "</body>")
        self.write_html_line(0, "</html>")

class SvgCanvas:
    def __init__(self, tlx: int, tly: int, rad: int) -> None:
        self.__tlx: int = tlx
        self.__tly: int = tly
        self.__w: int = w
        self.__h: int = h
        
class ArtConfig:
    BLUE: tuple = tuple((0, 255)) # default blue range

class GenRandom:
    @classmethod
    def gen_int_in_range(a: int, b: int) -> int:
        pass
    
    @classmethod
    def gen_float_in_range(a: float, b: float) -> float:
        pass

class Circle:
    def __init__(self, cx: int, cy: int, rad: int, red: int, green: int, blue: int, op: float) -> None:
        """shorten parameter list with nametuples"""
        self.__cx: int = cx
        self.__cy: int = cy
        self.__rad: int = rad
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op

    def draw_circle_line(hd: HtmlDoc, t: int) -> None:
        """draw_circle_line method"""
        ts: str = HtmlDoc.TAB * t
        line1: str = f'<circle cx="{self.__cx}" cy="{self.__cy}" r="{self.__rad}" '
        line2: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></circle>'
        hd.fd.write(f"{ts}{line1+line2}\n")

class Rectangle:
    pass


def main() -> None:
    hd: HtmlDoc = HtmlDoc("part1.html", "MyPart1")
    hd.open_html_file()
    hd.generate_html_file()
    hd.close_html_file()

if __name__ == "__main__":
    print(__doc__)
    main()
