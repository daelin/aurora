import React from 'react';
import styles from './style.scss';
import Modal from '../Modal';
import Kanban from '../Kanban';

export default class Feedback extends React.Component {
  componentWillReceiveProps(nextProps) {
    // if we changed routes...
    if (nextProps.location.key !== this.props.location.key
      && nextProps.location.state
      && nextProps.location.state.modal
    ) {
      // save the old children (just like animation)
      this.previousChildren = this.props.children
    }
  }

  render() {
    let {location} = this.props;
    let isModal = location.pathname.match(/^\/gsi\/feedback[/]*$/i) == null;

    return (
      <div>
        {isModal ?
          <Kanban /> :
          this.props.children
        }

        {isModal && (
          <Modal isOpen={true} returnTo="/gsi/feedback">
            {this.props.children}
          </Modal>
        )}
      </div>
    );
  }
}
