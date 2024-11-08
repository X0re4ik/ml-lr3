from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class DataProcessingUseCase:
    """Преобразование данных из файла (_input_file) в файл (_output_file)"""

    _input_file: Path
    _output_file: Path

    def execute(self):
        pre_df = pd.read_csv(self._input_file)
        df_cleaned = pre_df.drop("releaseYear", axis=1)
        df_cleaned.to_csv(self._output_file, index=False)


def get_data_processing_use_case(
    input_file: Path, output_file: Path
) -> DataProcessingUseCase:
    return DataProcessingUseCase(input_file, output_file)
