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

class InlineResponse2001(object):
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
        'type': 'str',
        'uuid': 'str',
        'tz': 'str',
        'start_at': 'datetime',
        'end_at': 'datetime',
        'created_at': 'datetime',
        'identity': 'InlineResponse2001Identity',
        'operator': 'InlineResponse2001Operator',
        'positions': 'list[Geopoint]',
        'driver': 'CertificateData',
        'passenger': 'CertificateData'
    }

    attribute_map = {
        'type': 'type',
        'uuid': 'uuid',
        'tz': 'tz',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'created_at': 'created_at',
        'identity': 'identity',
        'operator': 'operator',
        'positions': 'positions',
        'driver': 'driver',
        'passenger': 'passenger'
    }

    def __init__(self, type=None, uuid=None, tz=None, start_at=None, end_at=None, created_at=None, identity=None, operator=None, positions=None, driver=None, passenger=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._uuid = None
        self._tz = None
        self._start_at = None
        self._end_at = None
        self._created_at = None
        self._identity = None
        self._operator = None
        self._positions = None
        self._driver = None
        self._passenger = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid
        if tz is not None:
            self.tz = tz
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if created_at is not None:
            self.created_at = created_at
        if identity is not None:
            self.identity = identity
        if operator is not None:
            self.operator = operator
        if positions is not None:
            self.positions = positions
        if driver is not None:
            self.driver = driver
        if passenger is not None:
            self.passenger = passenger

    @property
    def type(self):
        """Gets the type of this InlineResponse2001.  # noqa: E501


        :return: The type of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2001.


        :param type: The type of this InlineResponse2001.  # noqa: E501
        :type: str
        """
        allowed_values = ["ok", "expired"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse2001.  # noqa: E501


        :return: The uuid of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse2001.


        :param uuid: The uuid of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def tz(self):
        """Gets the tz of this InlineResponse2001.  # noqa: E501


        :return: The tz of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._tz

    @tz.setter
    def tz(self, tz):
        """Sets the tz of this InlineResponse2001.


        :param tz: The tz of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._tz = tz

    @property
    def start_at(self):
        """Gets the start_at of this InlineResponse2001.  # noqa: E501


        :return: The start_at of this InlineResponse2001.  # noqa: E501
        :rtype: datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this InlineResponse2001.


        :param start_at: The start_at of this InlineResponse2001.  # noqa: E501
        :type: datetime
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this InlineResponse2001.  # noqa: E501


        :return: The end_at of this InlineResponse2001.  # noqa: E501
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this InlineResponse2001.


        :param end_at: The end_at of this InlineResponse2001.  # noqa: E501
        :type: datetime
        """

        self._end_at = end_at

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2001.  # noqa: E501


        :return: The created_at of this InlineResponse2001.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2001.


        :param created_at: The created_at of this InlineResponse2001.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def identity(self):
        """Gets the identity of this InlineResponse2001.  # noqa: E501


        :return: The identity of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Identity
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this InlineResponse2001.


        :param identity: The identity of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Identity
        """

        self._identity = identity

    @property
    def operator(self):
        """Gets the operator of this InlineResponse2001.  # noqa: E501


        :return: The operator of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this InlineResponse2001.


        :param operator: The operator of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Operator
        """

        self._operator = operator

    @property
    def positions(self):
        """Gets the positions of this InlineResponse2001.  # noqa: E501


        :return: The positions of this InlineResponse2001.  # noqa: E501
        :rtype: list[Geopoint]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this InlineResponse2001.


        :param positions: The positions of this InlineResponse2001.  # noqa: E501
        :type: list[Geopoint]
        """

        self._positions = positions

    @property
    def driver(self):
        """Gets the driver of this InlineResponse2001.  # noqa: E501


        :return: The driver of this InlineResponse2001.  # noqa: E501
        :rtype: CertificateData
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this InlineResponse2001.


        :param driver: The driver of this InlineResponse2001.  # noqa: E501
        :type: CertificateData
        """

        self._driver = driver

    @property
    def passenger(self):
        """Gets the passenger of this InlineResponse2001.  # noqa: E501


        :return: The passenger of this InlineResponse2001.  # noqa: E501
        :rtype: CertificateData
        """
        return self._passenger

    @passenger.setter
    def passenger(self, passenger):
        """Sets the passenger of this InlineResponse2001.


        :param passenger: The passenger of this InlineResponse2001.  # noqa: E501
        :type: CertificateData
        """

        self._passenger = passenger

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other