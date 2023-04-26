######################################################################################
# Copyright (c) 2018 - 2023 Orange - All Rights Reserved                             #
# * This software is the confidential and proprietary information of Orange.         #
# * You shall not disclose such Restricted Information and shall use it only in      #
#   accordance with the terms of the license agreement you entered into with Orange  #
#   named the "Khiops - Python Library Evaluation License".                          #
# * Unauthorized copying of this file, via any medium is strictly prohibited.        #
# * See the "LICENSE.md" file for more details.                                      #
######################################################################################
"""simplify_coclustering task family"""
from pykhiops.core.internals import task as tm
from pykhiops.core.internals.types import DictType, IntType, StringLikeType

# Disable long lines to have readable scenarios
# pylint: disable=line-too-long
TASKS = [
    tm.KhiopsTask(
        "simplify_coclustering",
        "khiops_coclustering",
        "10.1",
        [
            ("coclustering_file_path", StringLikeType),
            ("simplified_coclustering_file_path", StringLikeType),
            ("results_dir", StringLikeType),
        ],
        [
            ("max_preserved_information", IntType, 0),
            ("max_cells", IntType, 0),
            ("max_total_parts", IntType, 0),
            ("max_part_numbers", DictType(StringLikeType, IntType), None),
            ("results_prefix", StringLikeType, ""),
        ],
        [
            "coclustering_file_path",
            "simplified_coclustering_file_path",
            "results_dir",
        ],
        # fmt: off
        """
        // Simplify coclustering settings
        LearningTools.PostProcessCoclustering
        SelectInputCoclustering
        InputCoclusteringFileName __coclustering_file_path__
        OK
        PostProcessingSpec.MaxPreservedInformation __max_preserved_information__
        PostProcessingSpec.MaxCellNumber __max_cells__
        PostProcessingSpec.MaxTotalPartNumber __max_total_parts__
        __DICT__
        __max_part_numbers__
        PostProcessingSpec.PostProcessedAttributes.List.Key
        PostProcessingSpec.PostProcessedAttributes.MaxPartNumber
        __END_DICT__

        // Output settings
        AnalysisResults.ResultFilesDirectory __results_dir__
        AnalysisResults.ResultFilesPrefix __results_prefix__
        AnalysisResults.PostProcessedCoclusteringFileName __simplified_coclustering_file_path__

        // Simplify Coclustering
        PostProcessCoclustering
        Exit
        """,
        # fmt: on
    ),
    tm.KhiopsTask(
        "simplify_coclustering",
        "khiops_coclustering",
        "9.0",
        [
            ("coclustering_file_path", StringLikeType),
            ("simplified_coclustering_file_path", StringLikeType),
            ("results_dir", StringLikeType),
        ],
        [
            ("max_preserved_information", IntType, 0),
            ("max_cells", IntType, 0),
            ("max_part_numbers", DictType(StringLikeType, IntType), None),
            ("results_prefix", StringLikeType, ""),
        ],
        [
            "coclustering_file_path",
            "simplified_coclustering_file_path",
            "results_dir",
        ],
        # fmt: off
        """
        // Simplify coclustering settings
        LearningTools.PostProcessCoclustering
        SelectInputCoclustering
        InputCoclusteringFileName __coclustering_file_path__
        OK
        PostProcessingSpec.MaxPreservedInformation __max_preserved_information__
        PostProcessingSpec.MaxCellNumber __max_cells__
        __DICT__
        __max_part_numbers__
        PostProcessingSpec.PostProcessedAttributes.List.Key
        PostProcessingSpec.PostProcessedAttributes.MaxPartNumber
        __END_DICT__

        // Output settings
        AnalysisResults.ResultFilesDirectory __results_dir__
        AnalysisResults.ResultFilesPrefix __results_prefix__
        AnalysisResults.PostProcessedCoclusteringFileName __simplified_coclustering_file_path__

        // Simplify Coclustering
        PostProcessCoclustering
        Exit
        """,
        # fmt: on
    ),
]