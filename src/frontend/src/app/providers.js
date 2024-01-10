'use client';

import IBMHeader from './components/Header/Header';
import { Content, Theme } from '@carbon/react';

export function Providers({ children }) {
  return (
    <div>
      <Theme theme="g100">
        <IBMHeader />
      </Theme>
      <Content>{children}</Content>
    </div>
  );
}
