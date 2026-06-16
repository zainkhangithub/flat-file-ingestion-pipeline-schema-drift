class PipelineContext:
    def __init__(self, file_path, schema, df):
        self.file_path = file_path
        self.schema = schema
        self.df = df

        self.version = schema["version"]
        self.delimiter = schema["delimiter"]