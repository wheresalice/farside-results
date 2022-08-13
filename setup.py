from setuptools import setup

GIT_URL='https://github.com/wheresalice/farside-results'

setup(
        name = 'farside-results',
        version = '0.0.1',
        description = 'Redirect Searx results to farside',
        url = GIT_URL,
        author = 'wheresalice',
        license = 'GNU Affero General Public License',
        zip_safe = False,
        py_modules = [
            'farside_results'
            ],
        entry_points = {
            'searx.plugins' : [
                'wheresalice.farside-results = farside_results'
                ]
            }
        )
