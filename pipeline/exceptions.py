class PipelineError(Exception):
    """Base exception for pipeline errors."""
    pass


class SchemaDetectionError(PipelineError):
    """Schema could not be identified."""
    pass


class ValidationError(PipelineError):
    """Data validation failed."""
    pass


class FileFormatError(PipelineError):
    """Input file format is invalid."""
    pass