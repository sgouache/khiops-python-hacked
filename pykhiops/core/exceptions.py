######################################################################################
# Copyright (c) 2018 - 2023 Orange - All Rights Reserved                             #
# * This software is the confidential and proprietary information of Orange.         #
# * You shall not disclose such Restricted Information and shall use it only in      #
#   accordance with the terms of the license agreement you entered into with Orange  #
#   named the "Khiops - Python Library Evaluation License".                          #
# * Unauthorized copying of this file, via any medium is strictly prohibited.        #
# * See the "LICENSE.md" file for more details.                                      #
######################################################################################
"""pyKhiops exception classes"""


class PyKhiopsJSONError(Exception):
    """Parsing error for Khiops-generated JSON files"""


class PyKhiopsRuntimeError(Exception):
    """Khiops execution related errors"""


class PyKhiopsEnvironmentError(Exception):
    """PyKhiops execution environment error

    Example: Khiops binary not found.
    """