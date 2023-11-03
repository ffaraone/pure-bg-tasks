# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect_ext.events import Pure-Bg-TasksEventsApplication


def test_handle_asset_purchase_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = Pure-Bg-TasksEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'
