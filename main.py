from src.main import Main

if __name__ == "__main__":
    __import__('os').environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1"
    run = Main()
    run.main()
