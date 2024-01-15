import { Theme, FileUploader, Heading, Stack } from '@carbon/react';

`use client`;

export default function LandingPage() {
  return (
    <Theme theme="g10">
      <Stack gap={10} orientation="vertical">
        <div>
          <Heading>Generate Slides with WatsonX</Heading>
          Upload a summary email from a meeting and generate a presentation with
          the key point of the meeting.
        </div>

        <div className="uploader">
          <FileUploader
            labelTitle="Upload a summary email"
            labelDescription="Only a single .txt file is supported."
            buttonLabel="Upload File"
            buttonKind="primary"
            size="lg"
            filenameStatus="edit"
            type="file"
            accept={['.txt']}
            multiple={false}
            disabled={false}
            iconDescription="Delete file"
            name=""
            style={{ display: 'flex', alignItems: 'center' }}
            onChange={handleChange}
          />
        </div>
      </Stack>
    </Theme>
  );
}

function handleChange(event) {
  console.log(event.target.files[0]);
  const reader = new FileReader();
  reader.onload = async (e) => {
    const text = e.target.result;
    var jsonData = {
      text: text,
    };
    let url = 'http://localhost:5000';
    fetch(url, {
      method: 'POST',
      cache: 'no-cache',
      body: JSON.stringify(jsonData),
    })
      .then((res) => res.json())
      .then((response) => console.log('Success: ', response))
      .catch((error) => console.error('Error: ', error));
  };
  reader.readAsText(event.target.files[0]);
}
