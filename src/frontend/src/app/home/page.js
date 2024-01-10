import { Theme, FileUploader, Heading, Stack } from '@carbon/react';

`use client`;

export default function LandingPage() {
  return (
    <Stack gap={10} orientation="vertical">
      <div>
        <Heading>Generate Slides with WatsonX</Heading>
        Upload a summary email from a meeting and generate a presentation with
        the key point of the meeting.
      </div>

      <div className="uploader">
        <FileUploader
          labelTitle="Upload a summary email"
          labelDescription="Only .txt files are supported."
          buttonLabel="Add file"
          buttonKind="primary"
          filenameStatus="edit"
          accept={['.txt']}
          multiple={false}
          disabled={false}
          iconDescription="Delete file"
          name=""
          style={{ display: 'flex', alignItems: 'center' }}
        />
      </div>
    </Stack>
  );
}
