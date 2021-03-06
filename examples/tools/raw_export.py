from pipelines.image_pipeline import ImagePipeline
from pipelines.tools.export_dataset import ExportDatasetPipeline
from pipelines.tools.passthrough_model import PassthroughModelPipeline

# This class is used to test the direct storage of a dataset from the image pipeline.
class ImageRawExportPipeline(PassthroughModelPipeline, ExportDatasetPipeline, ImagePipeline):
    pass


if __name__ == "__main__":
    dataset_export_dir = "data/image_raw_export/out/"
    p = ImageRawExportPipeline(image_size=(150, 150), out_dir=None, max_content_length=4000000,
                               dataset_export_dir=dataset_export_dir)
    p.run()
