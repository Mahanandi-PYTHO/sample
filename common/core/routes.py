IGNORE_AUTH_ROUTES = [
    "/api/hrtech/auth/account/signin__POST",
    "/api/hrtech/auth/account/verify__POST",
    "/api/hrtech/auth/forgot/password__GET",
    "/api/hrtech/auth/forgot/password__POST",
]
IGNORE_PERMISSION_CHECK = [
    "/api/hrtech/auth/session/detail__GET",
    "/api/hrtech/auth/password/change__POST",
    "/api/hrtech/user/file/upload__POST",
    "/api/hrtech/user/files/__GET",
    "/api/hrtech/user/files/{id}/__GET",
]
AUTH_REQUIRED_ROUTES = {
    "staff__user": {
        "name": "EMPLOYEE PROFILE MANAGEMENT",
        "urls": {
            "staff/user/__GET": "Viewed Employees List",
            "staff/user/{id}/__GET": "Viewed Employee Detail",
            "staff/user/{id}/__PUT": "Updated Employee Details",
        }
    },
    "staff__user__onboard": {
        "name": "EMPLOYEE ONBOARD",
        "urls": {
            "staff/user/onboard/__POST": "Added New Employee"
        }
    },
    "cand__user": {
        "name": "CANDIDATE PROFILE MANAGEMENT",
        "urls": {
            "cand/user/__GET": "Viewed Candidates List",
            "cand/user/{id}/__GET": "Viewed Candidate Detail",
            "cand/user/{id}/__PUT": "Updated Candidate Details",
        }
    },
    "cand__user__onboard": {
        "name": "CANDIDATE ONBOARDING",
        "urls": {
            "cand/user/onboard/__POST": "Invited New Candidate"
        }
    },
    "cand__forms": {
        "name": "CANDIDATE PROFILE MANAGEMENT",
        "urls": {
            "cand/forms/__GET": "Viewed All Forms List",
            "cand/forms/__POST": "Filled Form Details",
            "cand/forms/{id}/__GET": "Viewed Form Detail",
            "cand/forms/{id}/__PUT": "Updated Form Details",
        }
    },
    "content__form": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/form/__GET": "Viewed Forms List",
            "content/form/__POST": "Added New Form",
            "content/form/{id}/__GET": "Viewed Form Detail",
            "content/form/{id}/__PUT": "Updated Form Details",
        }
    },
    "content__section": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/section/__GET": "Viewed Sections List",
            "content/section/__POST": "Added New Section",
            "content/section/{id}/__GET": "Viewed Section Detail",
            "content/section/{id}/__PUT": "Updated Section Details",
        }
    },
    "content__subsection": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/subsection/__GET": "Viewed SubSections List",
            "content/subsection/__POST": "Added New SubSection",
            "content/subsection/{id}/__GET": "Viewed SubSection Detail",
            "content/subsection/{id}/__PUT": "Updated SubSection Details",
        }
    },
    "content__formtypes": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/formtypes/__GET": "Viewed Form Types List",
            "content/formtypes/{id}/__GET": "Viewed Form Type Detail"
        }
    },
    "content__fields": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/fields/__GET": "Viewed Fields List",
            "content/fields/__POST": "Added New Fields",
            "content/fields/{id}/__GET": "Viewed Fields Detail",
            "content/fields/{id}/__PUT": "Updated Fields Details",
        }
    },
    "content__documents": {
        "name": "CONTENT MANAGEMENT",
        "urls": {
            "content/documents/__GET": "Viewed Documents List",
            "content/documents/__POST": "Added New Documents",
            "content/documents/{id}/__GET": "Viewed Documents Detail",
            "content/documents/{id}/__PUT": "Updated Documents Details",
        }
    },
    "cand__documents": {
        "name": "CANDIDATE PROFILE MANAGEMENT",
        "urls": {
            "content/documents/__GET": "Viewed Documents List",
            "content/documents/{id}/__GET": "Viewed Documents Detail",
        }
    },
}