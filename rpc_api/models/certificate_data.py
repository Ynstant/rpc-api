# coding: utf-8

"""
    API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: technique@covoiturage.beta.gouv.fr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CertificateData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'CertificateDataTotal',
        'trips': 'list[CertificateDataTrips]'
    }

    attribute_map = {
        'total': 'total',
        'trips': 'trips'
    }

    def __init__(self, total=None, trips=None):  # noqa: E501
        """CertificateData - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._trips = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if trips is not None:
            self.trips = trips

    @property
    def total(self):
        """Gets the total of this CertificateData.  # noqa: E501


        :return: The total of this CertificateData.  # noqa: E501
        :rtype: CertificateDataTotal
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CertificateData.


        :param total: The total of this CertificateData.  # noqa: E501
        :type: CertificateDataTotal
        """

        self._total = total

    @property
    def trips(self):
        """Gets the trips of this CertificateData.  # noqa: E501


        :return: The trips of this CertificateData.  # noqa: E501
        :rtype: list[CertificateDataTrips]
        """
        return self._trips

    @trips.setter
    def trips(self, trips):
        """Sets the trips of this CertificateData.


        :param trips: The trips of this CertificateData.  # noqa: E501
        :type: list[CertificateDataTrips]
        """

        self._trips = trips

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CertificateData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CertificateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
