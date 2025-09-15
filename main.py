from rich.console import Console

console = Console()


# TODO:1. create a default format
def tasks_separation(tasks: str, format: str) -> list[str]:
    # TODO:  2. pad the user input with _ until line is multiples of max line char
    task = tasks.split(format)
    return task


def main():
    task = tasks_separation(
        console.input("Input your task list: "), console.input("Input separator: ")
    )
    console.print(task)


if __name__ == "__main__":
    main()
