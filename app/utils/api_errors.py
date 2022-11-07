from fastapi import HTTPException


def raise_error_response(error, detail=None):
    error_body = dict(error.error)

    if detail is not None:
        error_body["detail"] = detail

    raise HTTPException(
        status_code=error.status_code,
        detail=error_body,
    )


class ErrorAuthenticationInvalid:
    status_code = 401

    error = {
        "type": "invalid_authentication",
        "description": "The authentication key provided is invalid.",
    }


class ErrorAuthorizationForbidden:
    status_code = 403

    error = {
        "type": "forbidden_authorization",
        "description": "The authentication "
        "key provided do not have permission to access this resource.",
    }


class ErrorResourceNotFound:
    status_code = 404

    error = {
        "type": "resource_not_found",
        "description": "The requested resource does not exist.",
    }


class ErrorResourceInvalid:
    status_code = 400

    error = {
        "type": "invalid_resource",
        "description": "The requested resource is invalid.",
    }


class ErrorInternal:
    status_code = 500

    error = {
        "type": "internal_error",
        "description": "An internal"
        " error has occurred while processing the request.",
    }


class BadRequest:
    status_code = 400

    error = {
        "type": "invalid_resource",
        "description": "The requested resource is invalid.",
    }
