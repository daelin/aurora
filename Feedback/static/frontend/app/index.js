import Moment from 'moment';
import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, IndexRoute, browserHistory} from 'react-router'

import Feedback from './components/Feedback';
import Kanban from './components/Kanban';
import {IssueDetail} from './components/Issue';


document.addEventListener("DOMContentLoaded", function (event) {
  Moment.locale('en');

  var node = document.getElementById('test');
  ReactDOM.render(
    (
      <Router history={browserHistory}>
        <Route path="/gsi/feedback" component={Feedback}>
          <IndexRoute component={Kanban} />
          <Route path="/gsi/feedback/issue/:id" component={IssueDetail} />
        </Route>
      </Router>
    ), node);
});
