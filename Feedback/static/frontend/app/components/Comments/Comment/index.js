import Moment from 'moment';
import React from 'react';
import CSSModules from 'react-css-modules';
import styles from './style.scss';

const url_regex = /(https?:\/\/[^\s]+)/g;

function Comment(props) {
  let comments = props.comment;
  comments = comments.replace(url_regex, url => {
    return `<a href="${url}">${url}</a>`;
  });

  const date = Moment.unix(props.post_date).calendar();

  return (
    <div styleName='comment'>
      <div styleName="header">
        <img styleName="pic" src={props.pic} />
        <span>{props.author}</span>&nbsp;
        <span styleName="date">on {date}</span>
      </div>
      <div styleName="body"
           dangerouslySetInnerHTML={{__html: comments}}></div>
    </div>
  );
}

export default CSSModules(Comment, styles)
