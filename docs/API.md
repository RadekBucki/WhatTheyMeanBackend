# Api module

## Description
This module is responsible for handling requests from frontend and returning responses. It is also responsible for
handling errors and returning proper error codes.

## Endpoints

### /analyse/<analyse_uuid>
#### Description
This endpoint is responsible for returning analyse by uuid.

#### Request
| Method | Content-Type | Body | Description |
|--------|--------------|------|-------------|
| GET    | application/json | - | This endpoint requires a uuid in the url. |

#### Response
| Status | Content-Type | Body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
|--------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 200    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"name": "Analysis",<br>&nbsp;&nbsp;&nbsp;&nbsp;"start_date": "2023-12-03T12:30:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"finish_date": "2023-12-03T15:45:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"status": "COMPLETED",<br>&nbsp;&nbsp;&nbsp;&nbsp;"file_type": "TIKTOK",<br>&nbsp;&nbsp;&nbsp;&nbsp;"link": "https://example.com/analysis", <br>&nbsp;&nbsp;&nbsp;&nbsp;"full_transcription": "This is the full transcription of the analysis.",<br>&nbsp;&nbsp;&nbsp;&nbsp;"video_summary": "A concise summary of the analysis video",<br>&nbsp;&nbsp;&nbsp;&nbsp;"author_attitude": "POSITIVE"<br>} | This endpoint returns a JSON object with three fields: transcription, sentiment, and summary. The transcription field contains a transcription of the video. The sentiment field contains a sentiment analysis of the video. The summary field contains a summary of the video. |
| 400    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"message": "Analysis with id 123dda not found in collection"<br>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This endpoint returns a JSON object with an error field. The error field contains an error message. |

### /analyse
#### Description
This endpoint is responsible for returning all analyses by list of uuids.

#### Request
| Method | Content-Type | Params     | Description |
|--------|--------------|------------|-------------|
| GET   | application/json | uuids:123d | This endpoint requires a JSON object with a uuids field. The uuids field should contain a list of uuids. |

#### Response
| Status | Content-Type | Body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
|--------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 200    | application/json | [{<br>&nbsp;&nbsp;&nbsp;&nbsp;"name": "Analysis",<br>&nbsp;&nbsp;&nbsp;&nbsp;"start_date": "2023-12-03T12:30:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"finish_date": "2023-12-03T15:45:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"status": "COMPLETED",<br>&nbsp;&nbsp;&nbsp;&nbsp;"file_type": "TIKTOK",<br>&nbsp;&nbsp;&nbsp;&nbsp;"link": "https://example.com/analysis", <br>&nbsp;&nbsp;&nbsp;&nbsp;"full_transcription": "This is the full transcription of the analysis.",<br>&nbsp;&nbsp;&nbsp;&nbsp;"video_summary": "A concise summary of the analysis video",<br>&nbsp;&nbsp;&nbsp;&nbsp;"author_attitude": "POSITIVE"<br>},<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;"name": "Analysis",<br>&nbsp;&nbsp;&nbsp;&nbsp;"start_date": "2023-12-03T12:30:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"finish_date": "2023-12-03T15:45:00",<br>&nbsp;&nbsp;&nbsp;&nbsp;"status": "COMPLETED",<br>&nbsp;&nbsp;&nbsp;&nbsp;"file_type": "TIKTOK",<br>&nbsp;&nbsp;&nbsp;&nbsp;"link": "https://example.com/analysis", <br>&nbsp;&nbsp;&nbsp;&nbsp;"full_transcription": "This is the full transcription of the analysis.",<br>&nbsp;&nbsp;&nbsp;&nbsp;"video_summary": "A concise summary of the analysis video",<br>&nbsp;&nbsp;&nbsp;&nbsp;"author_attitude": "POSITIVE"<br>}] | This endpoint returns a JSON object with three fields: transcription, sentiment, and summary. The transcription field contains a transcription of the video. The sentiment field contains a sentiment analysis of the video. The summary field contains a summary of the video. |
| 400    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"message": "Analysis with id 123dda not found in collection"<br>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This endpoint returns a JSON object with an error field. The error field contains an error message. |


### /register/file
#### Description
This endpoint is responsible for registering a new file for analysis.

#### Request
| Method | Content-Type | Body | Description |
|--------|--------------|------|-------------|
| POST   | multipart/form-data | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"file": "file"<br>} | This endpoint requires a file in the body. |

#### Response
| Status | Content-Type | Body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
|--------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 200    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"analysis_uuid": "123dda"<br>} | This endpoint returns a JSON object with a uuid field. The uuid field contains the uuid of the analysis. |
| 400    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"message": "No file part"<br>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This endpoint returns a JSON object with an error field. The error field contains an error message. |

### /register/link
#### Description
This endpoint is responsible for registering a new link for analysis.

#### Request
| Method | Content-Type | Body                                                                  | Description |
|--------|--------------|-----------------------------------------------------------------------|-------------|
| POST   | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"url": "https://example.com/video" <br>} | This endpoint requires a JSON object with a link field. The link field should contain a link to the video. |

#### Response
| Status | Content-Type | Body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
|--------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 200    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"analysis_uuid": "123dda"<br>} | This endpoint returns a JSON object with a uuid field. The uuid field contains the uuid of the analysis. |
| 400    | application/json | {<br>&nbsp;&nbsp;&nbsp;&nbsp;"message": "No url part"<br>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This endpoint returns a JSON object with an error field. The error field contains an error message. |
