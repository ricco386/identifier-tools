Identifier Tools
################

.. image:: https://gitlab.ore.nbs.sk/ore/identifier-tools/badges/master/pipeline.svg
  :alt: pipeline status

.. image:: https://gitlab.ore.nbs.sk/ore/identifier-tools/badges/master/coverage.svg
  :alt: coverage report

Library that helps working with different subject identifier types. Purpose of this library is to validate string
if it matches the identifier format and if possible calculate checksum if it is correct for identifier.

Identifier format checking is based on European Central Bank - `List of national identifiers
<https://www.ecb.europa.eu/stats/money/aggregates/anacredit/shared/pdf/List_of_national_identifiers.xlsx>`_ spreadsheet.

Identifier format is extended by identifiers issued by Národná banka Slovenska - `Národné voľby a špecifiká v projekte
AnaCredit <https://www.nbs.sk/sk/dohlad-nad-financnym-trhom-prakticke-informacie/zoznamy-subjektov-registre-a-formulare/registre/register-bankovych-uverov-a-zaruk-rbuz/projekt-anacredit>`_.

Curentlly supported identifiers for checksum calculation: IČO, IČO NI, LEI, NIČ, all available identifiers and their
format is listed in file `identifier_tools/formats.py <identifier_tools/formats.py>`_.

Identifier Tools library has support for ISO 7064 standard that is used to validate NIČ, LEI, IBAN among other things...
Read more at wikipedia: https://en.wikipedia.org/wiki/ISO_7064


Installation
------------

Install the released version::

    pip install identifier-tools

Alternatively you can install the package latest development version from the git repository::

    pip install https://gitlab.ore.nbs.sk/ore/identifier-tools/-/archive/master/identifier-tools-master.zip --trusted-host gitlab.ore.nbs.sk

Development
-----------

**We look forward to any kind of improvements and support for new identifiers.**

Clone a repository locally and make sure you work in your own branch and once you are happy with the functionality
create pull request. All new code should be covered with tests. We try to use test driven development for the project.

**If you find a bug feel free to create an issue with description**, how ever we appreciate even more if you create failing test.


Testing
=======

Tests are written in pytest and stored in tests directory. Library has 100% test coverage.
**If you found an error, write a failing test first.**

Run the tests by following command::

    pytest identifier_tools
