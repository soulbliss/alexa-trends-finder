import pyperclip
import click
from utils import helper_functions


################################################################################
################################ The Main Method ###############################
################################################################################

@click.command()

@click.option('--url','-u', type=str, default=pyperclip.paste(),
 help='Accepts the url that needs to be digged. You can have the link copied also.',
  prompt='Enter a valid url from alexa.com : ')
@click.option('--output_type','-o',type=str, prompt='Output mode. refer help for usage (-h) '
,help='l for Light analysis, d for in depth analysis', default='l')

def main(url,output_type):

    try:
        if output_type is 'l':
            helper_functions.light_analysis(url=url)
        elif output_type is 'd':
            helper_functions.in_depth_analysis(url=url)
        else:
            helper_functions.light_analysis(url=url)
    except Exception as e:
        print('Error raised : ' + str(e))


if __name__ == '__main__':
    main()
