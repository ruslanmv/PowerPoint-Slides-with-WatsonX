import './globals.scss';
import { Providers } from './providers';

export const metadata = {
  title: 'IBM PowerPoint Generator',
  description: 'IBM PowerPoint Generator',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
