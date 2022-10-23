import flet
from flet import ButtonStyle, Column, FilledButton, Page, Row, Text,TextField, colors
from flet.buttons import RoundedRectangleBorder
from flet.ref import Ref
from sentiment import get_sentiment

def main(page: Page):
    page.title = "Sentiment Analysis"
    page.padding = 50
    text = Ref[TextField]()
    result = Ref[Column]()
    
    def analyze(e):
        result.current.controls.append(Text(f"{get_sentiment(text.current.value)}!",size=20, weight="w600"))
        text.current.value = ""
        page.update()
        result.current.controls.pop()
    
    page.add(
    Row(
        [
            Text("Sentiment Analyzer", size=30, weight="bold"),
        ],
    ),
    Column(
        [
            TextField(ref=text, label="Text to analyze .",
multiline=True, width=700),
                FilledButton(
                    "Analyze",        

style=ButtonStyle(shape=RoundedRectangleBorder(radius=5), padding=14),
                    on_click=analyze,
              ),
              Column(ref=result),
              
        ]
    ),   
) 
    
    
flet.app(target=main)o