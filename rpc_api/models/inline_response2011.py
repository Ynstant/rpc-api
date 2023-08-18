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

class InlineResponse2011(object):
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
        'operator_journey_id': 'OperatorJourneyId',
        'created_at': 'datetime'
    }

    attribute_map = {
        'operator_journey_id': 'operator_journey_id',
        'created_at': 'created_at'
    }

    def __init__(self, operator_journey_id=None, created_at=None):  # noqa: E501
        """InlineResponse2011 - a model defined in Swagger"""  # noqa: E501
        self._operator_journey_id = None
        self._created_at = None
        self.discriminator = None
        self.operator_journey_id = operator_journey_id
        self.created_at = created_at

    @property
    def operator_journey_id(self):
        """Gets the operator_journey_id of this InlineResponse2011.  # noqa: E501


        :return: The operator_journey_id of this InlineResponse2011.  # noqa: E501
        :rtype: OperatorJourneyId
        """
        return self._operator_journey_id

    @operator_journey_id.setter
    def operator_journey_id(self, operator_journey_id):
        """Sets the operator_journey_id of this InlineResponse2011.


        :param operator_journey_id: The operator_journey_id of this InlineResponse2011.  # noqa: E501
        :type: OperatorJourneyId
        """
        if operator_journey_id is None:
            raise ValueError("Invalid value for `operator_journey_id`, must not be `None`")  # noqa: E501

        self._operator_journey_id = operator_journey_id

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2011.  # noqa: E501

        La date de création dans le registre  # noqa: E501

        :return: The created_at of this InlineResponse2011.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2011.

        La date de création dans le registre  # noqa: E501

        :param created_at: The created_at of this InlineResponse2011.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(InlineResponse2011, dict):
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
        if not isinstance(other, InlineResponse2011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
