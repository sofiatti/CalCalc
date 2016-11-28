import argparse
import xml.etree.ElementTree as et
import requests

APPID = 'W98948-A49G3PRWX5'

def parse():
    """Parse command line options"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='input query string', dest='q')
    parser.add_argument('-f', help='return the answer as a float',
                        dest='flt', action='store_true')
    return parser.parse_args()


def calculate(query, return_float=False):
    """Evaluates the input string with Wolfram Alpha API"""
    params = {'appid': APPID,
              'format': 'plaintext',
              'input': query}
    result = requests.get('http://api.wolframalpha.com/v2/query',
                          params=params)
    tree = et.fromstring(result.content)
    if tree.get('success') == 'false':
        return "ERROR: Wolfram Alpha didn't understand your query!"
    for pod in tree.iter('pod'):
        if pod.get('title') == 'Result':
            result_text = pod[0][0].text
            if not return_float:
                return result_text
            else:
                return text2float(result_text)
    return "ERROR: Wolfram Alpha didn't understand your query!"

def text2float(text):
    """Convert text with units to a float"""
    if text[0].isdigit():
        remove_unit = text.split()[0]
        if b'\xc3\x97' in remove_unit.encode():
            prefix, power = [x.decode() for x in remove_unit.encode().split(b'\xc3\x97')]
            base, exp = power.split('^')
            return float(prefix)*float(base)**float(exp)
        return float(remove_unit)
    print("Can't convert to float")
    return text

if __name__ == '__main__':
    args = parse()
    if args.q is not None:
        print(calculate(args.q, return_float=args.flt))
