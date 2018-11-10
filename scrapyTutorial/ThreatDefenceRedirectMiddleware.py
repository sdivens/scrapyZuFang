# -*- coding:utf-8 -*-
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware


class ThreatDefenceRedirectMiddleware(RedirectMiddleware):

    def _redirect(self, redirected, request, spider, reason):
        # 如果没有特殊的防范性重定向那就正常工作
        url1 = request.meta.get('redirect_urls', []) + \
        [request.url]
        if not self.is_threat_defense_url(url1):
            return super()._redirect(redirected, request, spider, reason)

        # logger.debug(f'Zipru threat defense triggered for {request.url}')
        return request

    def is_threat_defense_url(self, url):
        return 'http://zu.fang.com/house/' in url
