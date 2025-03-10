"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import copy
import time
from typing import Any, List

import reflex as rx

from .results import results
from .styles import question_style, page_background
import csv
import pandas as pd

from .utils import getAimeProblems

df_global = getAimeProblems(6)
print(df_global.shape)
#print(df_global)

class State(rx.State):
    """The app state."""

    default_answers = [None, None, None, None,None, None, None, None,None, None, None, None, None, None, None]
    answers: List[Any]
    answer_key = [None, None, None, None,None, None, None, None,None, None, None, None, None, None, None]
    df = df_global
    answer_key = df["Answer"].tolist()
    print('answer_key is ' + str(answer_key))
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index, sub_index=None):
        if index < len(self.answers):
            if sub_index is None:
                self.answers[index] = answer
            elif sub_index < len(self.answers[index]):
                self.answers[index][sub_index] = answer
            else:
                print(f"Sub-index {sub_index} out of range for answers[{index}]")
        else:
            print(f"Index {index} out of range for answers")

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            total += 1
        if total > 0:
            self.score = int(correct / total * 100)
        else:
            self.score = 0
            print("Total number of questions is zero, cannot calculate score.")
        return rx.redirect("/result")

    @rx.var
    def percent_score(self) -> str:
        return f"{self.score}%"


def header():
    return rx.vstack(
        rx.heading("Python Quiz"),
        rx.divider(),
        rx.text("Here is an example of a quiz made in Reflex."),
        rx.text("Once submitted the results will be shown in the results page."),
        style=question_style,
    )


def index():
    df = df_global
    #print(df)

    def generate_question(index, question_text):
        return rx.vstack(
            rx.heading(f"Question #{index + 1}"),
            rx.text("Solve the following equation for x:"),
            rx.markdown(question_text),
            rx.input(
                placeholder="Enter your answer here",
                on_change=lambda answer, idx=index: State.set_answers(answer, idx),
            ),
            rx.divider(),
        )

    questions = [generate_question(i, row["Problem latex"]) for i, row in df.iterrows()]

    return rx.color_mode.button(position="top-right"), rx.center(
        rx.vstack(
            header(),
            rx.vstack(
                *questions,
                rx.center(
                    rx.button("Submit", width="6em", on_click=State.submit),
                    width="100%",
                ),
                style=question_style,
                spacing="5",
            ),
            align="center",
        ),
        bg=page_background,
        padding_y="2em",
        min_height="100vh",
    )


def result():
    return rx.color_mode.button(position="top-right"), results(State)


def read_csv_and_print_first_rows(file_path, num_rows=10):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for i, row in enumerate(csv_reader):
            if i >= num_rows:
                break
            print(row)


def read_csv_to_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df


app = rx.App(
    theme=rx.theme(
        has_background=True, radius="none", accent_color="orange", appearance="light"
    ),
)
app.add_page(index, title="Quiz - Reflex", on_load=State.onload)
app.add_page(result, title="Quiz Results")
