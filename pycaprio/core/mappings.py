DATE_FORMAT_ISO8601 = "%Y-%m-%dT%H:%M:%S%z"
NO_PROJECT = -1
NO_DOCUMENT = -1


class DocumentFormats:
    DEFAULT = 'text'
    TEXT = 'text'


class DocumentStatus:
    DEFAULT = 'NEW'
    NEW = 'NEW'
    LOCKED = 'LOCKED'
    IN_PROGRESS = 'IN-PROGRESS'
    COMPLETE = 'COMPLETE'


class AnnotationStatus:
    DEFAULT = 'ANNOTATION-IN-PROGRESS'
    ANNOTATION_IN_PROGRESS = 'ANNOTATION-IN-PROGRESS'
    ANNOTATION_COMPLETE = 'ANNOTATION-COMPLETE'
    CURATION_IN_PROGRESS = 'CURATION-IN-PROGRESS'
    CURATION_COMPLETE = 'CURATION-COMPLETE'
