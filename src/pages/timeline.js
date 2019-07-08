import React from 'react'
import { Link, StaticQuery, graphql } from 'gatsby'

import Bio from '../components/Bio'
import Layout from '../components/Layout'
import SEO from '../components/seo'
import { rhythm } from '../utils/typography'

class Timeline extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title

    const examples = data.allExampleJson.edges

    function getSidebarLabels(data) {

	  const sidebarItemsArray = data.allGoodreadsJson.edges.map(item => {
		const elt = (
			<li key={item.node.book_id}>
				<img src={item.node.image_url} alt={item.node.title} />
				<span>{item.node.date_started}:{item.node.date_finished}</span>
				&nbsp;
				<span>({item.node.number_of_pages})</span>
				<a href={`https://goodreads.com/book/show/${item.node.book_id}`}>
				  {item.node.title}
				</a>
			</li>);
	    return elt;
	  });
	  return sidebarItemsArray;
	}

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <SEO
          title="Timeline"
          keywords={[`blog`, `gatsby`, `javascript`, `react`]}
        />
        <Bio />
	    <>
	       <ul>{getSidebarLabels(data)}</ul>
	    </>
      </Layout>
    )
  }
}

export default Timeline

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
	allExampleJson {
	  edges {
		node {
		  label
	    }
	  }
	}
	allGoodreadsJson(sort: {fields: date_finished, order: DESC}) {
	  edges {
	    node {
	  	book_id
	  	title
	  	image_url
	  	date_started
	  	date_finished
		number_of_pages
	    }
	  }
	}

  }
`
