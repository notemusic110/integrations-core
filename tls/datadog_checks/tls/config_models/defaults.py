# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_allowed_versions(field, value):
    return get_default_field_value(field, value)


def shared_fetch_intermediate_certs(field, value):
    return False


def shared_service(field, value):
    return get_default_field_value(field, value)


def instance_allowed_versions(field, value):
    return get_default_field_value(field, value)


def instance_days_critical(field, value):
    return 7.0


def instance_days_warning(field, value):
    return 14.0


def instance_empty_default_hostname(field, value):
    return False


def instance_fetch_intermediate_certs(field, value):
    return False


def instance_intermediate_cert_refresh_interval(field, value):
    return 60


def instance_local_cert_path(field, value):
    return get_default_field_value(field, value)


def instance_min_collection_interval(field, value):
    return 15


def instance_name(field, value):
    return get_default_field_value(field, value)


def instance_port(field, value):
    return 443


def instance_seconds_critical(field, value):
    return get_default_field_value(field, value)


def instance_seconds_warning(field, value):
    return get_default_field_value(field, value)


def instance_send_cert_duration(field, value):
    return False


def instance_server_hostname(field, value):
    return get_default_field_value(field, value)


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_timeout(field, value):
    return 10


def instance_tls_ca_cert(field, value):
    return get_default_field_value(field, value)


def instance_tls_cert(field, value):
    return get_default_field_value(field, value)


def instance_tls_private_key(field, value):
    return get_default_field_value(field, value)


def instance_tls_private_key_password(field, value):
    return get_default_field_value(field, value)


def instance_tls_validate_hostname(field, value):
    return True


def instance_tls_verify(field, value):
    return True


def instance_transport(field, value):
    return 'TCP'
