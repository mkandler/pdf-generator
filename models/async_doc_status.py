# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AsyncDocStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncDocStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'download_url': 'str',
            'download_id': 'str',
            'message': 'str',
            'number_of_pages': 'int',
            'validation_errors': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'download_url': 'download_url',
            'download_id': 'download_id',
            'message': 'message',
            'number_of_pages': 'number_of_pages',
            'validation_errors': 'validation_errors'
        }

        self._status = None
        self._download_url = None
        self._download_id = None
        self._message = None
        self._number_of_pages = None
        self._validation_errors = None

    @property
    def status(self):
        """
        Gets the status of this AsyncDocStatus.
        The present status of the document. Can be queued, working, completed, and failed.

        :return: The status of this AsyncDocStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AsyncDocStatus.
        The present status of the document. Can be queued, working, completed, and failed.

        :param status: The status of this AsyncDocStatus.
        :type: str
        """
        self._status = status

    @property
    def download_url(self):
        """
        Gets the download_url of this AsyncDocStatus.
        The URL where the document can be retrieved. This URL may only be used a few times.

        :return: The download_url of this AsyncDocStatus.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this AsyncDocStatus.
        The URL where the document can be retrieved. This URL may only be used a few times.

        :param download_url: The download_url of this AsyncDocStatus.
        :type: str
        """
        self._download_url = download_url

    @property
    def download_id(self):
        """
        Gets the download_id of this AsyncDocStatus.
        The identifier for downloading the document with the download api.

        :return: The download_id of this AsyncDocStatus.
        :rtype: str
        """
        return self._download_id

    @download_id.setter
    def download_id(self, download_id):
        """
        Sets the download_id of this AsyncDocStatus.
        The identifier for downloading the document with the download api.

        :param download_id: The download_id of this AsyncDocStatus.
        :type: str
        """
        self._download_id = download_id

    @property
    def message(self):
        """
        Gets the message of this AsyncDocStatus.
        Additional information.

        :return: The message of this AsyncDocStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AsyncDocStatus.
        Additional information.

        :param message: The message of this AsyncDocStatus.
        :type: str
        """
        self._message = message

    @property
    def number_of_pages(self):
        """
        Gets the number_of_pages of this AsyncDocStatus.
        Number of PDF pages in document.

        :return: The number_of_pages of this AsyncDocStatus.
        :rtype: int
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        """
        Sets the number_of_pages of this AsyncDocStatus.
        Number of PDF pages in document.

        :param number_of_pages: The number_of_pages of this AsyncDocStatus.
        :type: int
        """
        self._number_of_pages = number_of_pages

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this AsyncDocStatus.
        Error information.

        :return: The validation_errors of this AsyncDocStatus.
        :rtype: str
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this AsyncDocStatus.
        Error information.

        :param validation_errors: The validation_errors of this AsyncDocStatus.
        :type: str
        """
        self._validation_errors = validation_errors

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

