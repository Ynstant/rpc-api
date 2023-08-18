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

class InlineResponse200(object):
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
        'distance': 'Distance',
        'duration': 'Duration'
    }

    attribute_map = {
        'distance': 'distance',
        'duration': 'duration'
    }

    def __init__(self, distance=None, duration=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._distance = None
        self._duration = None
        self.discriminator = None
        self.distance = distance
        self.duration = duration

    @property
    def distance(self):
        """Gets the distance of this InlineResponse200.  # noqa: E501


        :return: The distance of this InlineResponse200.  # noqa: E501
        :rtype: Distance
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this InlineResponse200.


        :param distance: The distance of this InlineResponse200.  # noqa: E501
        :type: Distance
        """
        if distance is None:
            raise ValueError("Invalid value for `distance`, must not be `None`")  # noqa: E501

        self._distance = distance

    @property
    def duration(self):
        """Gets the duration of this InlineResponse200.  # noqa: E501


        :return: The duration of this InlineResponse200.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse200.


        :param duration: The duration of this InlineResponse200.  # noqa: E501
        :type: Duration
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
