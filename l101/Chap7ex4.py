def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def main():
    try:
        some_function()
    except UnicodeError:
        print("unicode error happening now")
    except ValueError:
        print("value error happening now")

if __name__ == "__main__":
    main()

