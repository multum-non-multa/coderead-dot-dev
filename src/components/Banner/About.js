import React from 'react'
import SocialLinks from '../../constants/socialLinks'
import { StaticImage } from 'gatsby-plugin-image'
import Title from './Title'
import styled from 'styled-components'

const About = () => {
  return (
    <Wrapper>
      <Title title="Earlier Posts" />
      <a href="https://multum-non-multa.github.io/code/">
        <StaticImage
          src="../../assets/CODEREAD.jpeg"
          layout="fixed"
          width={100}
          height={100}
          alt="about description"
          className="img"
        />
      </a>

      <div>
        <p>Click on Alfred E. Neumann for Earlier Posts</p>
      </div>

      {/* <SocialLinks styleClass="banner-icons" /> */}
    </Wrapper>
  )
}

const Wrapper = styled.div`
  text-align: center;
  p {
    color: var(--clr-grey-5);
  }
  .img {
    border-radius: 50%;
    margin: 0 auto;
    margin-bottom: 1rem;
  }
`
export default About
