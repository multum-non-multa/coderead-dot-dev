import React from 'react'
import Highlight, { defaultProps } from 'prism-react-renderer'
import theme from 'prism-react-renderer/themes/nightOwlLight'
import styled from 'styled-components'

const PrismWrapper = props => {
  const className = props.children.props.className
  const language = className.split('-')[1]

  return (
    <Highlight
      {...defaultProps}
      code={props.children.props.children.trim()}
      language={language}
      theme={theme}
    >
      {({ className, style, tokens, getLineProps, getTokenProps }) => {
        return (
          <Container>
            <Pre className={className} style={style}>
              <div className="code-tab">{language}</div>
              {tokens.map((line, i) => (
                <div {...getLineProps({ line, key: i })}>
                  {line.map((token, key) => (
                    <span {...getTokenProps({ token, key })} />
                  ))}
                </div>
              ))}
            </Pre>
          </Container>
        )
      }}
    </Highlight>
  )
}
// Styling Only
const Pre = styled.pre`
  /* background attributes appear to be superseded somewhere */
  background: #1e1e1e;
  background-color: #1e1e1e;
  padding: 1rem 1.2rem;
  border-radius: var(--radius);
  /* trk */
  border: 1px solid rgba(100, 100, 100, 0.1);
  margin: 2.5rem 0;
  /* font-size: 0.9rem; */
  /* trk */
  font-size: 1rem;
  /* trk */
  font-weight: 600;
  /* font-family: 'Courier New', Courier, monospace; */
  font-family: Monaco, Courier, monospace;
  overflow-x: scroll;
  .token-line {
    line-height: 1.5;
  }
  .code-tab {
    position: absolute;
    top: 0;
    right: 5%;
    color: rgb(156, 220, 254);
    font-size: 0.8rem;
    font-weight: 600;
    transform: translateY(-100%);
    text-transform: uppercase;
    text-transform: lowercase;
    padding: 0.05rem 0.85rem 0;
    /* aen */
    padding: 0.05rem 1rem 0;
    border-top-left-radius: var(--radius);
    border-top-right-radius: var(--radius);
    background: #1e1e1e;
    background: #000;
  }
`
const Container = styled.article`
  position: relative;
`

export default PrismWrapper
