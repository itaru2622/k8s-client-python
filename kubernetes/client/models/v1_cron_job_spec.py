# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.28
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1CronJobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'concurrency_policy': 'str',
        'failed_jobs_history_limit': 'int',
        'job_template': 'V1JobTemplateSpec',
        'schedule': 'str',
        'starting_deadline_seconds': 'int',
        'successful_jobs_history_limit': 'int',
        'suspend': 'bool',
        'time_zone': 'str'
    }

    attribute_map = {
        'concurrency_policy': 'concurrencyPolicy',
        'failed_jobs_history_limit': 'failedJobsHistoryLimit',
        'job_template': 'jobTemplate',
        'schedule': 'schedule',
        'starting_deadline_seconds': 'startingDeadlineSeconds',
        'successful_jobs_history_limit': 'successfulJobsHistoryLimit',
        'suspend': 'suspend',
        'time_zone': 'timeZone'
    }

    def __init__(self, concurrency_policy=None, failed_jobs_history_limit=None, job_template=None, schedule=None, starting_deadline_seconds=None, successful_jobs_history_limit=None, suspend=None, time_zone=None, local_vars_configuration=None):  # noqa: E501
        """V1CronJobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._concurrency_policy = None
        self._failed_jobs_history_limit = None
        self._job_template = None
        self._schedule = None
        self._starting_deadline_seconds = None
        self._successful_jobs_history_limit = None
        self._suspend = None
        self._time_zone = None
        self.discriminator = None

        if concurrency_policy is not None:
            self.concurrency_policy = concurrency_policy
        if failed_jobs_history_limit is not None:
            self.failed_jobs_history_limit = failed_jobs_history_limit
        self.job_template = job_template
        self.schedule = schedule
        if starting_deadline_seconds is not None:
            self.starting_deadline_seconds = starting_deadline_seconds
        if successful_jobs_history_limit is not None:
            self.successful_jobs_history_limit = successful_jobs_history_limit
        if suspend is not None:
            self.suspend = suspend
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def concurrency_policy(self):
        """Gets the concurrency_policy of this V1CronJobSpec.  # noqa: E501

        Specifies how to treat concurrent executions of a Job. Valid values are:  - \"Allow\" (default): allows CronJobs to run concurrently; - \"Forbid\": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - \"Replace\": cancels currently running job and replaces it with a new one  # noqa: E501

        :return: The concurrency_policy of this V1CronJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_policy

    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy):
        """Sets the concurrency_policy of this V1CronJobSpec.

        Specifies how to treat concurrent executions of a Job. Valid values are:  - \"Allow\" (default): allows CronJobs to run concurrently; - \"Forbid\": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - \"Replace\": cancels currently running job and replaces it with a new one  # noqa: E501

        :param concurrency_policy: The concurrency_policy of this V1CronJobSpec.  # noqa: E501
        :type: str
        """

        self._concurrency_policy = concurrency_policy

    @property
    def failed_jobs_history_limit(self):
        """Gets the failed_jobs_history_limit of this V1CronJobSpec.  # noqa: E501

        The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.  # noqa: E501

        :return: The failed_jobs_history_limit of this V1CronJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._failed_jobs_history_limit

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit):
        """Sets the failed_jobs_history_limit of this V1CronJobSpec.

        The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.  # noqa: E501

        :param failed_jobs_history_limit: The failed_jobs_history_limit of this V1CronJobSpec.  # noqa: E501
        :type: int
        """

        self._failed_jobs_history_limit = failed_jobs_history_limit

    @property
    def job_template(self):
        """Gets the job_template of this V1CronJobSpec.  # noqa: E501


        :return: The job_template of this V1CronJobSpec.  # noqa: E501
        :rtype: V1JobTemplateSpec
        """
        return self._job_template

    @job_template.setter
    def job_template(self, job_template):
        """Sets the job_template of this V1CronJobSpec.


        :param job_template: The job_template of this V1CronJobSpec.  # noqa: E501
        :type: V1JobTemplateSpec
        """
        if self.local_vars_configuration.client_side_validation and job_template is None:  # noqa: E501
            raise ValueError("Invalid value for `job_template`, must not be `None`")  # noqa: E501

        self._job_template = job_template

    @property
    def schedule(self):
        """Gets the schedule of this V1CronJobSpec.  # noqa: E501

        The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.  # noqa: E501

        :return: The schedule of this V1CronJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this V1CronJobSpec.

        The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.  # noqa: E501

        :param schedule: The schedule of this V1CronJobSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def starting_deadline_seconds(self):
        """Gets the starting_deadline_seconds of this V1CronJobSpec.  # noqa: E501

        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.  # noqa: E501

        :return: The starting_deadline_seconds of this V1CronJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._starting_deadline_seconds

    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds):
        """Sets the starting_deadline_seconds of this V1CronJobSpec.

        Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.  # noqa: E501

        :param starting_deadline_seconds: The starting_deadline_seconds of this V1CronJobSpec.  # noqa: E501
        :type: int
        """

        self._starting_deadline_seconds = starting_deadline_seconds

    @property
    def successful_jobs_history_limit(self):
        """Gets the successful_jobs_history_limit of this V1CronJobSpec.  # noqa: E501

        The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.  # noqa: E501

        :return: The successful_jobs_history_limit of this V1CronJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._successful_jobs_history_limit

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit):
        """Sets the successful_jobs_history_limit of this V1CronJobSpec.

        The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.  # noqa: E501

        :param successful_jobs_history_limit: The successful_jobs_history_limit of this V1CronJobSpec.  # noqa: E501
        :type: int
        """

        self._successful_jobs_history_limit = successful_jobs_history_limit

    @property
    def suspend(self):
        """Gets the suspend of this V1CronJobSpec.  # noqa: E501

        This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.  # noqa: E501

        :return: The suspend of this V1CronJobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1CronJobSpec.

        This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.  # noqa: E501

        :param suspend: The suspend of this V1CronJobSpec.  # noqa: E501
        :type: bool
        """

        self._suspend = suspend

    @property
    def time_zone(self):
        """Gets the time_zone of this V1CronJobSpec.  # noqa: E501

        The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones  # noqa: E501

        :return: The time_zone of this V1CronJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this V1CronJobSpec.

        The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones  # noqa: E501

        :param time_zone: The time_zone of this V1CronJobSpec.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CronJobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CronJobSpec):
            return True

        return self.to_dict() != other.to_dict()
