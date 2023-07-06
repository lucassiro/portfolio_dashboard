from st_pages import Page, show_pages

show_pages(
    [
        Page("pages/home/main.py", "Home", ":house:"),
        Page("pages/image_classification/main.py", "Computer Vision", ":house:"),
        # Page("pages/finance/main.py", "Finance", ":house:")
    ]
)
