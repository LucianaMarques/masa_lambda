from argparse import ArgumentParser

from lambda_launcher import LambdaLauncher


if __name__ == '__main__':
    parser = ArgumentParser(prog="MASAExecutionOnLambda",
                        description="Program to execute MASA-OpenMP in ",
                        epilog="Some final message") #TODO: edit epilog
    parser.add_argument('--register_function', default=False)
    parser.add_argument('--invoke_function', default=False)
    parser.add_argument('--update_function', default=False)

    args = parser.parse_args()

    launcher = LambdaLauncher()
    try:
        if (args.update_function):
            launcher.update_function_code("masa-function", "./masa_function.zip")
        elif (args.invoke_function):
            launcher.invoke_masa_function()
    except Exception as ex:
        print(f'Lambda launcher failed with exception: {ex}')