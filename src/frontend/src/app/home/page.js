import { Button, Theme } from '@carbon/react';
import {
  FileUploader,
  FileUploaderButton,
  FileUploaderDropContainer,
  FileUploaderItem,
  FileUploaderSkeleton,
} from '@carbon/react';

`use client`;

export default function LandingPage() {
  return (
    <Theme theme="g100">
      <section className="theme-section">
        <FileUploader
          labelTitle="Upload files"
          labelDescription="Max file size is 500mb. Only .txt files are supported."
          buttonLabel="Add file"
          buttonKind="primary"
          size="md"
          filenameStatus="edit"
          accept={['.txt']}
          multiple={true}
          disabled={false}
          iconDescription="Delete file"
          name=""
          style={{ display: 'flex', alignItems: 'center' }}
        />
      </section>
    </Theme>
  );
}
