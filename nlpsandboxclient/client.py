"""NLP data node client that interacts with the SDK datanodeclient"""
from typing import List

import datanode

DATA_NODE_HOST = "http://10.23.55.45:8080/api/v1"


def get_notes(host: str, dataset_id: str, fhir_store_id: str) -> List[dict]:
    """Get all clinical notes for a dataset

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        fhir_store_id: FHIR store Id

    Returns:
        list of clinical notes.

    Examples:
        >>> notes = get_notes(host="0.0.0.0/api/v1",
        >>>                   dataset_id="awesome-dataset",
        >>>                   fhir_store_id="awesome-fhir-store")
        >>> notes[0]
        {
            "id": "noteid",
            "noteType": "",
            "patientId": "patient_id",
            "text": "Example text",
            "note_name": "dataset/awesome-dataset/fhirStores/awesome-fhirstore/fhir/Note/noteid"
        }
    """
    configuration = datanode.Configuration(host=host)
    all_notes = []
    offset=0
    limit=10
    with datanode.ApiClient(configuration) as api_client:
        note_api = datanode.NoteApi(api_client)
        # Obtain all clinical notes
        next_page = True
        while next_page:
            notes = note_api.list_notes(dataset_id, fhir_store_id,
                                        offset=offset, limit=limit)
            for note in notes.notes:
                all_notes.append({
                    "id": note.id,
                    "noteType": note.note_type,
                    "patientId": note.patient_id,
                    "text": note.text,
                    "note_name": f"dataset/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Note/{note.id}"
                })
            next_page = notes.links.next
            offset += limit
    return all_notes


def store_annotation(host: str, dataset_id: str, annotation_store_id: str,
                     annotation: dict) -> datanode.models.Annotation:
    """Store annotation

    Args:
        host: Data node host IP
        dataset_id: Dataset Id
        annotation_store_id: Annotation store Id
        annotation: Annotation dict

    Returns:
        Data node Annotation object

    Examples:
        >>> example_annotation = {
        >>>     "annotationSource": {
        >>>         "resourceSource": {
        >>>             "name": "name"
        >>>         }
        >>>     },
        >>>     "textDateAnnotations": [
        >>>         {
        >>>             "dateFormat": "MM/DD/YYYY",
        >>>             "length": 10,
        >>>             "start": 42,
        >>>             "text": "10/26/2020"
        >>>         },
        >>>         {
        >>>             "dateFormat": "MM/DD/YYYY",
        >>>             "length": 10,
        >>>             "start": 42,
        >>>             "text": "10/26/2020"
        >>>         }
        >>>     ],
        >>>     "textPersonNameAnnotations": [],
        >>>     "textPhysicalAddressAnnotations": []
        >>> }
        >>> annotation = store_annotation(host="0.0.0.0/api/v1",
        >>>                               dataset_id="awesome-dataset",
        >>>                               annotation_store_id="awesome-annotation-store",
        >>>                               annotation=example_annotation)

    """
    configuration = datanode.Configuration(host=host)
    with datanode.ApiClient(configuration) as api_client:
        annotation_api = datanode.AnnotationApi(api_client)
        annotation_obj = annotation_api.create_annotation(
            dataset_id=dataset_id,
            annotation_store_id=annotation_store_id,
            annotation=annotation
        )
    return annotation_obj
