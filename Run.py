import unittest
import time

import HTMLTestRunner

if __name__ == '__main__':
    mSuit = unittest.TestLoader().discover('testcases','*.py');
    reportName = time.strftime('%y%m%d%H%M%S');
    fp = open('reports/'+reportName+'.html', 'wb');
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'cnote接口测试报告',
        description=''
    )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    #runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(mSuit);